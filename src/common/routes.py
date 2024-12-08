import importlib.util
from pathlib import Path

from fastapi import APIRouter

from src.common.logger import logger


def load_routes():
    routes = []
    modules_path = Path(__file__).parent.parent / 'modules'
    if not modules_path.exists():
        logger.warning(f"Modules path does not exist: {modules_path}")
        return routes

    for module_file in modules_path.glob('*.py'):

        try:
            spec = importlib.util.spec_from_file_location(
                module_file.stem,
                str(module_file)
            )
            if spec and spec.loader:
                module = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(module)

                if hasattr(module, 'router') and isinstance(module.router, APIRouter):
                    logger.info(f"Loaded route from module: {module_file.name}")
                    routes.append(module.router)
        except Exception as e:
            logger.error(f"Module loading error {module_file}: {str(e)}")

    return routes
