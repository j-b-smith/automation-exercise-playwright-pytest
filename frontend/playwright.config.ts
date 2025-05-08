import { defineConfig, devices } from '@playwright/test';
import dotenv from 'dotenv';

// Read from .env file
dotenv.config();

// Define environment variables with fallbacks
const BASE_URL = process.env.BASE_URL || 'https://www.automationexercise.com';
const API_BASE_URL = process.env.API_BASE_URL || 'https://www.automationexercise.com/api';

/**
 * See https://playwright.dev/docs/test-configuration
 */
export default defineConfig({
  testDir: './tests',
  timeout: 30 * 1000, // 30 seconds timeout for tests
  expect: {
    timeout: 5000 // 5 seconds timeout for assertions
  },
  fullyParallel: true, // Run tests in parallel
  forbidOnly: !!process.env.CI, // Fail if test.only is used in CI
  retries: process.env.CI ? 2 : 0, // Retry on CI only
  workers: process.env.CI ? 1 : undefined, // Opt out of parallel tests on CI
  reporter: [
    ['html', { outputFolder: 'test-results/html-report' }],
    ['list'],
    ['junit', { outputFile: 'test-results/junit-report.xml' }]
  ],
  use: {
    baseURL: BASE_URL,
    trace: 'on-first-retry', // Record trace on the first retry of failed tests
    screenshot: 'only-on-failure', // Take screenshots only on failure
    video: 'on-first-retry', // Record video only on the first retry
    // Browser configurations
    headless: true,
    viewport: { width: 1280, height: 720 },
    ignoreHTTPSErrors: true,
    actionTimeout: 10000 // 10 seconds timeout for actions
  },
  projects: [
    {
      name: 'chromium',
      use: { ...devices['Desktop Chrome'] }
    },
    {
      name: 'firefox',
      use: { ...devices['Desktop Firefox'] }
    },
    {
      name: 'webkit',
      use: { ...devices['Desktop Safari'] }
    },
    {
      name: 'Mobile Chrome',
      use: { ...devices['Pixel 5'] }
    },
    {
      name: 'Mobile Safari',
      use: { ...devices['iPhone 12'] }
    }
  ],
  outputDir: 'test-results/test-output',
});