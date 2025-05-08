# Automation Exercise Test Framework

A comprehensive automated testing framework for [Automation Exercise](https://www.automationexercise.com) website using both API and UI testing approaches.

## Overview

This project implements a dual-layer testing approach:

1. **Backend API Testing**: Using Python with Pytest and Requests library
2. **Frontend UI Testing**: Using TypeScript with Playwright

The framework follows best practices such as the Page Object Model (POM) pattern, data-driven testing, and comprehensive logging.

## Project Structure

```
├── backend/                     # Backend API tests
│   ├── api/                     # API client and endpoints
│   ├── config/                  # Configuration settings
│   ├── data/                    # Test data
│   ├── tests/                   # Test cases
│   └── utils/                   # Helper utilities
├── frontend/                    # Frontend UI tests
│   ├── src/
│   │   ├── data/                # Test data 
│   │   ├── fixtures/            # Test fixtures
│   │   ├── pages/               # Page objects
│   │   └── utils/               # Helper utilities
│   └── tests/                   # Test cases
└── .gitignore
```

## Backend Testing

### Setup

1. Install dependencies:
   ```bash
   cd backend
   pip install -r requirements.txt
   ```

2. Configure environment variables (optional):
   Create a `.env` file in the backend directory:
   ```
   BASE_URL=https://www.automationexercise.com
   API_BASE_URL=https://www.automationexercise.com/api
   DEFAULT_TIMEOUT=30
   ```

### Running Tests

Execute all tests:
```bash
cd backend
pytest
```

Run specific test categories:
```bash
pytest -m api          # Run API tests only
pytest -m smoke        # Run smoke tests only
```

Generate HTML report:
```bash
pytest --html=report.html
```

### Backend Features

- Comprehensive API client with logging
- Data-driven test approach with dynamic test data generation
- Detailed HTML test reports
- Modular and extensible architecture

## Frontend Testing

### Setup

1. Install dependencies:
   ```bash
   cd frontend
   npm install
   ```

2. Configure environment variables (optional):
   Create a `.env` file in the frontend directory:
   ```
   BASE_URL=https://www.automationexercise.com
   API_BASE_URL=https://www.automationexercise.com/api
   ```

### Running Tests

Execute all tests:
```bash
cd frontend
npm run test
```

Run tests in a specific browser:
```bash
npm run test:chrome    # Run tests in Chrome
npm run test:firefox   # Run tests in Firefox
npm run test:webkit    # Run tests in Safari
```

Run tests in UI mode:
```bash
npm run test:ui
```

Run tests in headed mode:
```bash
npm run test:headed
```

Generate and view report:
```bash
npm run report
```

### Frontend Features

- Page Object Model implementation for maintainable tests
- Cross-browser testing support
- TypeScript for type safety
- Dynamic test data generation
- Visual test reporting

## Test Cases

### User Authentication Tests

1. **Register User**: Complete user registration flow
2. **Login with Valid Credentials**: Login with correct email/password
3. **Login with Invalid Credentials**: Verify error handling for incorrect login
4. **Logout**: Verify logout functionality
5. **Register with Existing Email**: Verify duplicate email validation

Additional test cases include testing invalid email formats, incorrect passwords, and various error scenarios.

## Maintenance

Both backend and frontend frameworks are designed to be maintainable and extensible:

- Add new API endpoints in `backend/api/api_endpoints.py`
- Add new API methods in `backend/api/api_methods.py`
- Create new page objects in `frontend/src/pages/`
- Add new test cases in `backend/tests/` or `frontend/tests/`


## License

MIT