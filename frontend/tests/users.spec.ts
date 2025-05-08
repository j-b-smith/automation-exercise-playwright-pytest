// tests/users.spec.ts
import { test, expect } from '../src/fixtures/setup';
import { LoginSignupPage } from '../src/pages/LoginSignupPage';
import { SignupPage } from '../src/pages/SignupPage';
import { HomePage } from '../src/pages/HomePage';
import { generateRandomUser } from '../src/utils/helpers';
import { Page } from '@playwright/test';

test('should register user successfully', async ({ page }: { page: Page }) => {
  const homePage = new HomePage(page);
  const loginSignupPage = new LoginSignupPage(page);
  const signupPage = new SignupPage(page);
  
  const testUser = generateRandomUser();
  
  await homePage.goToHomePage();
  const title = await page.title();
  expect(title).toContain('Automation Exercise');
  
  await homePage.goToLoginSignupPage();
  await expect(loginSignupPage.newUserSignupText).toBeVisible();
  
  await loginSignupPage.signupWithNameAndEmail(testUser.name, testUser.email);
  await expect(signupPage.accountInfoTitle).toBeVisible();
  
  await signupPage.fillAccountInformation(testUser);
  expect(await signupPage.isAccountCreatedMessageVisible()).toBeTruthy();
  
  await signupPage.continueAfterAccountCreation();
  expect(await homePage.isUserLoggedIn(testUser.name)).toBeTruthy();
  
  await homePage.deleteAccount();
});

test('should login user with correct credentials', async ({ page }: { page: Page }) => {
  const homePage = new HomePage(page);
  const loginSignupPage = new LoginSignupPage(page);
  const signupPage = new SignupPage(page);
  
  const testUser = generateRandomUser();
  
  await homePage.goToHomePage();
  await homePage.goToLoginSignupPage();
  await loginSignupPage.signupWithNameAndEmail(testUser.name, testUser.email);
  await signupPage.fillAccountInformation(testUser);
  await expect(signupPage.accountCreatedMessage).toBeVisible();
  await signupPage.continueAfterAccountCreation();
  await homePage.logout();
  
  await homePage.goToHomePage();
  
  const title = await page.title();
  expect(title).toContain('Automation Exercise');
  
  await homePage.goToLoginSignupPage();
  await expect(loginSignupPage.loginToAccountText).toBeVisible();
  
  await loginSignupPage.login(testUser.email, testUser.password);
  expect(await homePage.isUserLoggedIn(testUser.name)).toBeTruthy();
  
  await homePage.deleteAccount();
});

test('should not allow login with invalid credentials', async ({ page }: { page: Page }) => {
  const homePage = new HomePage(page);
  const loginSignupPage = new LoginSignupPage(page);
  
  await homePage.goToHomePage();
  
  const title = await page.title();
  expect(title).toContain('Automation Exercise');
  
  await homePage.goToLoginSignupPage();
  await expect(loginSignupPage.loginToAccountText).toBeVisible();
  
  await loginSignupPage.login('incorrect@example.com', 'wrongpassword');
  expect(await loginSignupPage.isErrorMessageDisplayed()).toBeTruthy();
});

test('should not allow login with correct email but wrong password', async ({ page }: { page: Page }) => {
  const homePage = new HomePage(page);
  const loginSignupPage = new LoginSignupPage(page);
  const signupPage = new SignupPage(page);
  
  const testUser = generateRandomUser();
  
  await homePage.goToHomePage();
  await homePage.goToLoginSignupPage();
  await loginSignupPage.signupWithNameAndEmail(testUser.name, testUser.email);
  await signupPage.fillAccountInformation(testUser);
  await expect(signupPage.accountCreatedMessage).toBeVisible();
  await signupPage.continueAfterAccountCreation();
  await homePage.logout();
  
  await homePage.goToHomePage();
  await homePage.goToLoginSignupPage();
  await expect(loginSignupPage.loginToAccountText).toBeVisible();
  
  await loginSignupPage.login(testUser.email, 'wrongpassword123');
  expect(await loginSignupPage.isErrorMessageDisplayed()).toBeTruthy();
});

test('should allow user to logout', async ({ page }: { page: Page }) => {
  const homePage = new HomePage(page);
  const loginSignupPage = new LoginSignupPage(page);
  const signupPage = new SignupPage(page);
  
  const testUser = generateRandomUser();
  
  await homePage.goToHomePage();
  await homePage.goToLoginSignupPage();
  await loginSignupPage.signupWithNameAndEmail(testUser.name, testUser.email);
  await signupPage.fillAccountInformation(testUser);
  await expect(signupPage.accountCreatedMessage).toBeVisible();

  await signupPage.continueAfterAccountCreation();
  expect(await homePage.isUserLoggedIn(testUser.name)).toBeTruthy();
  
  await homePage.logout();
  await expect(loginSignupPage.loginToAccountText).toBeVisible();
});

test('should not allow registration with existing email', async ({ page }: { page: Page }) => {
  const homePage = new HomePage(page);
  const loginSignupPage = new LoginSignupPage(page);
  const signupPage = new SignupPage(page);
  
  const testUser = generateRandomUser();
  
  await homePage.goToHomePage();
  await homePage.goToLoginSignupPage();
  await loginSignupPage.signupWithNameAndEmail(testUser.name, testUser.email);
  await signupPage.fillAccountInformation(testUser);
  await expect(signupPage.accountCreatedMessage).toBeVisible();
  await signupPage.continueAfterAccountCreation();
  await homePage.logout();
  
  await homePage.goToHomePage();
  
  const title = await page.title();
  expect(title).toContain('Automation Exercise');
  
  await homePage.goToLoginSignupPage();
  await expect(loginSignupPage.newUserSignupText).toBeVisible();

  await loginSignupPage.signupWithNameAndEmail('Another User', testUser.email);
  expect(await signupPage.isEmailExistsErrorVisible()).toBeTruthy();
});