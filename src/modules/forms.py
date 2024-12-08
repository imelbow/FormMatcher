from fastapi import APIRouter, Request, Body, HTTPException
from typing import Dict, Union
from src.common.validators import FieldValidator
from src.common.logger import logger
from src.common.docs import api_docs

router = APIRouter(tags=["forms"])
validator = FieldValidator()


@router.post(
    path="/get_form",
    response_model=Union[Dict[str, str], Dict[str, str]],
    summary=api_docs["get_form"]["summary"],
    description=api_docs["get_form"]["description"],
    responses=api_docs["get_form"]["responses"],
    openapi_extra={
        "requestBody": {
            "content": {
                "application/json": {
                    "examples": api_docs["get_form"]["requestBody"]["content"]["application/json"]["examples"]
                },
                "multipart/form-data": {
                    "examples": api_docs["get_form"]["requestBody"]["content"]["multipart/form-data"]["examples"]
                }
            }
        }
    }
)
async def get_form(request: Request):
    content_type = request.headers.get('content-type', '')
    
    try:
        if 'application/json' in content_type:
            form_data = await request.json()
        elif 'multipart/form-data' in content_type:
            form = await request.form()
            form_data = dict(form)
        elif 'application/x-www-form-urlencoded' in content_type:
            form = await request.form()
            form_data = dict(form)
        else:
            raise HTTPException(status_code=415, detail="Unsupported media type")

        if not form_data:
            raise HTTPException(status_code=400, detail="Empty form data")
            
        logger.debug(f"Received form data: {form_data}")
        
        try:
            db = request.state.db
            templates = db.form_templates.find()
            templates_list = list(templates)
        except Exception as e:
            logger.error(f"Database error: {str(e)}")
            raise HTTPException(status_code=500, detail="Database error")

        for template in templates_list:
            matches = True
            for field_name, field_type in template['fields'].items():
                if field_name not in form_data:
                    logger.debug(f"Field {field_name} not found in form data")
                    matches = False
                    break
                
                value = str(form_data[field_name]).strip()
                if field_type == 'email' and not validator.validate_email(value):
                    matches = False
                    break
                elif field_type == 'phone' and not validator.validate_phone(value):
                    matches = False
                    break
                elif field_type == 'date' and not validator.validate_date(value):
                    matches = False
                    break

            if matches:
                return {"template_name": template['name']}

        # Если шаблон не найден, определяем типы полей
        field_types = {}
        for field_name, value in form_data.items():
            value = str(value).strip()
            field_types[field_name] = validator.determine_field_type(value)

        return field_types
    except Exception as e:
        logger.error(f"Error parsing form data: {str(e)}")
        raise HTTPException(status_code=400, detail="Invalid form data")
