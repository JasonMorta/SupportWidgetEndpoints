from aiohttp import web
from aiohttp_middlewares import cors_middleware
from routes import setup_routes
from middleware import main_middleware
from aiohttp_middlewares import error_middleware, timeout_middleware

def create_app():
    # Define allowed origins for CORS
    cors_config = {
        "*": {  # This allows all origins
            "allow_credentials": True,
            "allow_methods": ["GET", "POST", "OPTIONS"],  # Specify allowed HTTP methods
            "allow_headers": ["api-key", "date", "Content-Type", "Authorization"],  # Allowed headers
            "expose_headers": ["Content-Type"],  # Headers that can be exposed to the browser
        }
    }

    # Create the application
    app = web.Application()

    # Add custom middleware
    app.middlewares.append(main_middleware)

    # Add CORS middleware allowing all origins
    app.middlewares.append(cors_middleware(
        allow_all=True,  # Allow all origins
        origins=cors_config  # Still specifying the allowed methods and headers
    ))

    # Add timeout middleware (optional)
    # app.middlewares.append(timeout_middleware(29.5))  # Set request timeout at 29.5 seconds

    # Setup application routes
    setup_routes(app)

    return app
