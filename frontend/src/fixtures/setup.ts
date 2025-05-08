import { test as base } from '@playwright/test';
import { BasePage } from '../pages/BasePage';

// This is the correct way to extend fixtures in Playwright
type CustomFixtures = {
  basePage: BasePage;
};

// Extend the base test fixture with custom fixtures
export const test = base.extend<CustomFixtures>({
  /**
   * Base page fixture
   */
  basePage: async ({ page }, use) => {
    const basePage = new BasePage(page);
    await use(basePage);
  }
});

export { expect } from '@playwright/test';