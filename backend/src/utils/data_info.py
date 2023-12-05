from src.schemas.status_endpoints import StatusEndpoints
from src.schemas.http_method import HTTPMethod

MODEL_DESCRIPTION = "This is a web service that allows you to analyze the sentiment of a given text. It also allows you to analyze the text in a more complete way, including extra information like Parts of Speech, Named Entities Recognition and Embeddings."

SERVICE_ENDPOINTS = [
    StatusEndpoints(
        path="/status",
        description="Get the status of the service",
        method=HTTPMethod.GET,
    ),
    StatusEndpoints(
        path="/sentiment",
        description="Get the sentiment of a given text",
        method=HTTPMethod.POST,
    ),
    StatusEndpoints(
        path="/analysis",
        description="Get a complete analysis of a given text",
        method=HTTPMethod.POST
    ),
    StatusEndpoints(
        path="/reports",
        description="Get the reports of the service",
        method=HTTPMethod.GET
    )
]