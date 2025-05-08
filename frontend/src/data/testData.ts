import { faker } from '@faker-js/faker';
import { generateRandomUser, generateRandomPaymentDetails } from '../utils/helpers';

/**
 * Fixed test user data for scenarios that need consistent data
 */
export const fixedTestUser = {
  name: 'Test User',
  email: 'test.user@example.com',
  password: 'password123',
  title: 'Mr',
  birthDate: '1',
  birthMonth: 'January',
  birthYear: '1990',
  firstName: 'Test',
  lastName: 'User',
  company: 'Test Company',
  address1: '123 Test Street',
  address2: 'Apt 456',
  country: 'United States',
  state: 'California',
  city: 'Los Angeles',
  zipcode: '90001',
  mobileNumber: '1234567890'
};

/**
 * Dynamic test user data that changes on import
 * Use this for tests that need unique user data
 */
export const testUser = generateRandomUser();

/**
 * Payment data
 */
export const paymentDetails = generateRandomPaymentDetails();

/**
 * Product search data
 */
export const searchProducts = {
  validProduct: faker.helpers.arrayElement(['dress', 'top', 'tshirt', 'jeans']),
  invalidProduct: `invalid${faker.string.alphanumeric(10)}`
};