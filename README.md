# Order Status Management API

## Task Overview

An e-commerce company needs reliable visibility into the status of customer orders as they move through fulfillment (e.g., created, shipped, delivered, cancelled). Business users have reported that valid status updates (like 'shipped') are being rejected with validation errors, causing delays and customer confusion. The current backend exposes endpoints for updating order statuses but is not correctly handling valid status values.

## Guidance

You are working on a FastAPI and PostgreSQL backend that provides endpoints for updating an order's status. Ensure the API uses consistent status values, leveraging Pydantic enums for request and response validation as well as proper SQLAlchemy integration for persistence. Keep business logic and data access separated. Use dependency injection for database sessions. Implement robust error handling and return appropriate HTTP status codes for invalid status values. Containerize the app for consistent local and team environments using Docker and Docker Compose. Adhere to best practices for environment variable management and modular code structure.

## Objectives

- Implement the endpoint to update an order's status, accepting only valid status values (e.g., 'created', 'shipped', 'delivered', 'cancelled')
- Align Pydantic enum validation and SQLAlchemy models to support these values
- Ensure successful updates are persisted to the database and reflected in API responses
- Handle invalid status values with clear error messages and appropriate status codes
- Use async/await for all database operations
- Provide OpenAPI documentation via FastAPI
- Secure all service-to-database configuration using environment variables

## How to Verify

- The order status update endpoint accepts valid status values and updates the order in the database
- Providing an invalid status value returns a 422 error with a descriptive validation error
- The API response includes the updated status and order data
- The application runs successfully in Docker Compose with both API and PostgreSQL services healthy
- OpenAPI documentation accurately reflects the allowed order status values
