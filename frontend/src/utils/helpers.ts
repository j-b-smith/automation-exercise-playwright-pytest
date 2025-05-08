import { faker } from '@faker-js/faker';

/**
 * Generate random string
 * @param length Length of random string
 * @returns Random string
 */
export function generateRandomString(length: number = 10): string {
  return faker.string.alphanumeric(length);
}

/**
 * Generate random email
 * @returns Random email
 */
export function generateRandomEmail(): string {
  return faker.internet.email();
}

/**
 * Get current date in format DD-MM-YYYY
 * @returns Current date
 */
export function getCurrentDate(): string {
  const date = new Date();
  const day = String(date.getDate()).padStart(2, '0');
  const month = String(date.getMonth() + 1).padStart(2, '0');
  const year = date.getFullYear();
  return `${day}-${month}-${year}`;
}

/**
 * Sleep for specified time
 * @param ms Time in milliseconds
 * @returns Promise
 */
export function sleep(ms: number): Promise<void> {
  return new Promise(resolve => setTimeout(resolve, ms));
}

/**
 * Get random number between min and max
 * @param min Minimum number
 * @param max Maximum number
 * @returns Random number
 */
export function getRandomNumber(min: number, max: number): number {
  return faker.number.int({ min, max });
}

/**
 * Generate random user data
 * @returns Random user data object
 */
export function generateRandomUser() {
  const firstName = faker.person.firstName();
  const lastName = faker.person.lastName();
  
  return {
    name: `${firstName} ${lastName}`,
    email: faker.internet.email({ firstName, lastName }),
    password: faker.internet.password({ length: 12 }),
    title: faker.helpers.arrayElement(['Mr', 'Mrs', 'Miss']),
    birthDate: String(faker.number.int({ min: 1, max: 28 })),
    birthMonth: faker.date.month(),
    birthYear: String(faker.number.int({ min: 1970, max: 2000 })),
    firstName,
    lastName,
    company: faker.company.name(),
    address1: faker.location.streetAddress(),
    address2: faker.location.secondaryAddress(),
    country: 'United States',
    state: faker.location.state(),
    city: faker.location.city(),
    zipcode: faker.location.zipCode(),
    mobileNumber: faker.phone.number()
  };
}

/**
 * Generate random payment details
 * @returns Random payment details object
 */
export function generateRandomPaymentDetails() {
  return {
    nameOnCard: faker.person.fullName(),
    cardNumber: faker.finance.creditCardNumber(),
    cvc: faker.finance.creditCardCVV(),
    expiryMonth: String(faker.number.int({ min: 1, max: 12 })),
    expiryYear: String(faker.number.int({ min: new Date().getFullYear(), max: new Date().getFullYear() + 10 }))
  };
}
