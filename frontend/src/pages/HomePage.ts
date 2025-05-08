import { Page, Locator, expect } from '@playwright/test';
import { BasePage } from './BasePage';

export class HomePage extends BasePage {
  readonly homeLink: Locator;
  readonly productsLink: Locator;
  readonly cartLink: Locator;
  readonly loginLink: Locator;
  readonly testCasesLink: Locator;
  readonly apiTestingLink: Locator;
  readonly videoTutorialsLink: Locator;
  readonly contactUsLink: Locator;
  readonly loggedInAsText: Locator;
  readonly logoutLink: Locator;
  readonly deleteAccountLink: Locator;
  readonly accountDeletedMessage: Locator;
  readonly continueButton: Locator;

  constructor(page: Page) {
    super(page);
    
    this.homeLink = page.locator('a', { hasText: ' Home' });
    this.productsLink = page.locator('a', { hasText: ' Products' });
    this.cartLink = page.locator('a', { hasText: ' Cart' });
    this.loginLink = page.locator('a', { hasText: ' Signup / Login' });
    this.testCasesLink = page.locator('a', { hasText: ' Test Cases' });
    this.apiTestingLink = page.locator('a', { hasText: ' API Testing' });
    this.videoTutorialsLink = page.locator('a', { hasText: ' Video Tutorials' });
    this.contactUsLink = page.locator('a', { hasText: ' Contact us' });
    this.loggedInAsText = page.locator('a', { hasText: ' Logged in as ' });
    this.logoutLink = page.locator('a', { hasText: ' Logout' });
    this.deleteAccountLink = page.locator('a', { hasText: ' Delete Account' });
    this.accountDeletedMessage = page.locator('h2.title', { hasText: 'Account Deleted!' });
    this.continueButton = page.locator('[data-qa="continue-button"]');
  }
  
  async goToHomePage(): Promise<void> {
    await this.goto('/');
  }
  
  async goToLoginSignupPage(): Promise<void> {
    await this.loginLink.click();
  }
  
  async isUserLoggedIn(username?: string): Promise<boolean> {
    if (username) {
      return await this.page.locator('a', { hasText: ` Logged in as ${username}` }).isVisible();
    }
    return await this.loggedInAsText.isVisible();
  }
  
  async logout(): Promise<void> {
    await this.logoutLink.click();
  }
  
  async deleteAccount(): Promise<void> {
    await this.deleteAccountLink.click();
    await this.continueButton.click();
  }
}