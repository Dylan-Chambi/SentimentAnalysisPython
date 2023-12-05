from src.schemas.status import Status
from src.schemas.status_endpoints import StatusEndpoints
from src.config.config import get_settings
from src.utils.data_info import MODEL_DESCRIPTION, SERVICE_ENDPOINTS

SETTINGS = get_settings()

def get_service_status() -> Status:
    response: Status = Status(
        title=SETTINGS.api_name,
        description=MODEL_DESCRIPTION,
        models_used=[SETTINGS.sentiment_model, SETTINGS.spacy_model],
        endpoints=SERVICE_ENDPOINTS
    )
    return response