// src/theme.ts
import { createTheme } from '@mantine/core';

export const crumblePrimary = [
  '#f4ebe2',
  '#729b79', // main primary color
  '#ce8964',
  '#832232',
  '#370031',
  '#0b0033',
  '#2c1f12',
  '#1a1410',
  '#f4cd0b',
  '#050302',
] as const;

export const crumbleSecondary = '#f4cd0b';
export const crumbleTertiary = '#832232';
export const crumbleBackground = '#f4ebe2';
export const crumbleFontColor = '#0b0033';

const crumbleTheme = createTheme({
  fontFamily: 'Inter, sans-serif',
  colors: { primary: crumblePrimary },
  primaryColor: 'primary',
  defaultRadius: 'md',
  headings: {
    fontFamily: 'Inter, sans-serif',
    sizes: {
      h1: { fontSize: '2.2rem', fontWeight: '600' },
      h2: { fontSize: '1.6rem', fontWeight: '600' },
    },
  },
  components: {
    Button: {
      styles: {
        root: { fontWeight: 500 },
      },
    },
    Card: {
      styles: {
        root: { backgroundColor: crumbleBackground },
      },
    },
  },
});

export default crumbleTheme;