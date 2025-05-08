import { Page, Locator, expect } from '@playwright/test';
import { BasePage } from './BasePage';

export class LoginSignupPage extends BasePage {
  readonly signupNameInput: Locator;
  readonly signupEmailInput: Locator;
  readonly signupButton: Locator;
  readonly loginEmailInput: Locator;
  readonly loginPasswordInput: Locator;
  readonly loginButton: Locator;
  readonly loginForm: Locator;
  readonly signupForm: Locator;
  readonly errorMessage: Locator;
  readonly newUserSignupText: Locator;
  readonly loginToAccountText: Locator;
  readonly logoutLink: Locator;
  readonly deleteAccountLink: Locator;
  
  constructor(page: Page) {
    super(page);
    
    this.signupNameInput = page.locator('[data-qa="signup-name"]');
    this.signupEmailInput = page.locator('[data-qa="signup-email"]');
    this.signupButton = page.locator('[data-qa="signup-button"]');
    this.loginEmailInput = page.locator('[data-qa="login-email"]');
    this.loginPasswordInput = page.locator('[data-qa="login-password"]');
    this.loginButton = page.locator('[data-qa="login-button"]');
    this.loginForm = page.locator('.login-form');
    this.signupForm = page.locator('.signup-form');
    this.errorMessage = page.locator('.login-form p', { hasText: 'Your email or password is incorrect!' });
    this.newUserSignupText = page.locator('h2', { hasText: 'New User Signup!' });
    this.loginToAccountText = page.locator('h2', { hasText: 'Login to your account' });
    this.logoutLink = page.locator('a', { hasText: ' Logout' });
    this.deleteAccountLink = page.locator('a', { hasText: ' Delete Account' });
  }
  
  /**
   * Navigate to login/signup page
   */
  async goToLoginSignupPage(): Promise<void> {
    await this.goto('/login');
    await expect(this.newUserSignupText).toBeVisible();
    await expect(this.loginToAccountText).toBeVisible();
  }
  
  /**
   * Sign up with name and email
   * @param name User name
   * @param email User email
   */
  async signupWithNameAndEmail(name: string, email: string): Promise<void> {
    await this.signupNameInput.fill(name);
    await this.signupEmailInput.fill(email);
    await this.signupButton.click();
  }
  
  /**
   * Log in with email and password
   * @param email User email
   * @param password User password
   */
  async login(email: string, password: string): Promise<void> {
    await this.loginEmailInput.fill(email);
    await this.loginPasswordInput.fill(password);
    await this.loginButton.click();
  }
  
  /**
   * Check if error message is displayed
   * @returns Promise resolving to boolean
   */
  async isErrorMessageDisplayed(): Promise<boolean> {
    return await this.errorMessage.isVisible();
  }
  
  /**
   * Logout
   */
  async logout(): Promise<void> {
    await this.logoutLink.click();
  }
  
  /**
   * Delete account
   */
  async deleteAccount(): Promise<void> {
    await this.deleteAccountLink.click();
  }
}