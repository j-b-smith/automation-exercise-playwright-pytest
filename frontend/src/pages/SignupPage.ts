import { Page, Locator, expect } from '@playwright/test';
import { BasePage } from './BasePage';

export class SignupPage extends BasePage {
  readonly accountInfoTitle: Locator;
  readonly titleMr: Locator;
  readonly titleMrs: Locator;
  readonly name: Locator;
  readonly email: Locator;
  readonly password: Locator;
  readonly dayOfBirth: Locator;
  readonly monthOfBirth: Locator;
  readonly yearOfBirth: Locator;
  readonly newsletterCheckbox: Locator;
  readonly specialOffersCheckbox: Locator;
  readonly firstName: Locator;
  readonly lastName: Locator;
  readonly company: Locator;
  readonly address1: Locator;
  readonly address2: Locator;
  readonly country: Locator;
  readonly state: Locator;
  readonly city: Locator;
  readonly zipcode: Locator;
  readonly mobileNumber: Locator;
  readonly createAccountButton: Locator;
  readonly accountCreatedMessage: Locator;
  readonly continueButton: Locator;
  readonly existingEmailError: Locator;
  
  constructor(page: Page) {
    super(page);
    
    this.accountInfoTitle = page.locator('h2.title', { hasText: 'Enter Account Information' });
    this.titleMr = page.locator('#id_gender1');
    this.titleMrs = page.locator('#id_gender2');
    this.name = page.locator('#name');
    this.email = page.locator('#email');
    this.password = page.locator('#password');
    this.dayOfBirth = page.locator('#days');
    this.monthOfBirth = page.locator('#months');
    this.yearOfBirth = page.locator('#years');
    this.newsletterCheckbox = page.locator('#newsletter');
    this.specialOffersCheckbox = page.locator('#optin');
    this.firstName = page.locator('#first_name');
    this.lastName = page.locator('#last_name');
    this.company = page.locator('#company');
    this.address1 = page.locator('#address1');
    this.address2 = page.locator('#address2');
    this.country = page.locator('#country');
    this.state = page.locator('#state');
    this.city = page.locator('#city');
    this.zipcode = page.locator('#zipcode');
    this.mobileNumber = page.locator('#mobile_number');
    this.createAccountButton = page.locator('[data-qa="create-account"]');
    this.accountCreatedMessage = page.locator('h2.title', { hasText: 'Account Created!' });
    this.continueButton = page.locator('[data-qa="continue-button"]');
    this.existingEmailError = page.locator('.signup-form p', { hasText: 'Email Address already exist!' });
  }
  
  /**
   * Fill account information
   * @param userData User data object
   */
  async fillAccountInformation(userData: any): Promise<void> {
    await expect(this.accountInfoTitle).toBeVisible();
    
    if (userData.title === 'Mr') {
      await this.titleMr.check();
    } else {
      await this.titleMrs.check();
    }
    
    await expect(this.name).toHaveValue(userData.name);
    await expect(this.email).toHaveValue(userData.email);
    await this.password.fill(userData.password);
    
    await this.dayOfBirth.selectOption(userData.birthDate);
    await this.monthOfBirth.selectOption(userData.birthMonth);
    await this.yearOfBirth.selectOption(userData.birthYear);
    
    await this.newsletterCheckbox.check();
    await this.specialOffersCheckbox.check();
    
    await this.firstName.fill(userData.firstName);
    await this.lastName.fill(userData.lastName);
    await this.company.fill(userData.company);
    await this.address1.fill(userData.address1);
    await this.address2.fill(userData.address2);
    await this.country.selectOption(userData.country);
    await this.state.fill(userData.state);
    await this.city.fill(userData.city);
    await this.zipcode.fill(userData.zipcode);
    await this.mobileNumber.fill(userData.mobileNumber);
    
    await this.createAccountButton.click();
  }
  
  /**
   * Check if account created message is visible
   * @returns Promise resolving to boolean
   */
  async isAccountCreatedMessageVisible(): Promise<boolean> {
    return await this.accountCreatedMessage.isVisible();
  }
  
  /**
   * Continue after account creation
   */
  async continueAfterAccountCreation(): Promise<void> {
    await this.continueButton.click();
  }
  
  /**
   * Check if email already exists error is visible
   * @returns Promise resolving to boolean
   */
  async isEmailExistsErrorVisible(): Promise<boolean> {
    return await this.existingEmailError.isVisible();
  }
}