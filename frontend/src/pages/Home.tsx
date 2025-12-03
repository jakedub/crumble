import { Container, Group, ActionIcon, Text } from '@mantine/core';
import { useLocalStorage, useHotkeys } from '@mantine/hooks';
import { IconSun, IconMoon } from '@tabler/icons-react';
import { motion } from 'framer-motion';
import type { Variants } from 'framer-motion';
import { crumblePrimary } from '../theme';
import Cookie from '../components/Cookie';

export default function HomePage() {
  const [colorScheme, setColorScheme] = useLocalStorage<'light' | 'dark'>({
    key: 'mantine-color-scheme',
    defaultValue: 'light',
  });

  // ✅ Fixed syntax here
  const toggleColorScheme = (value?: 'light' | 'dark') =>
    setColorScheme(value || (colorScheme === 'dark' ? 'light' : 'dark'));

  useHotkeys([['mod+J', () => toggleColorScheme()]]);

  const features = ['Recipes', 'Inventory', 'COGs', 'Dashboard', 'R&D', 'Label Maker', 'Test'];

  const cardVariants: Variants = {
    offscreen: { y: 50, opacity: 0, scale: 0.9 },
    onscreen: {
      y: 0,
      opacity: 1,
      scale: 1,
      transition: { type: 'spring', bounce: 0.3, duration: 0.7 },
    },
  };

  return (
    <Container
      style={{
        minHeight: '100vh',
        display: 'flex',
        flexDirection: 'column',
        justifyContent: 'center',
        alignItems: 'center',
        textAlign: 'center',
        padding: 'var(--mantine-spacing-xl)',
      }}
    >
      {/* Dark mode toggle */}
      <Group
        style={{
          justifyContent: 'flex-end',
          marginBottom: 'var(--mantine-spacing-md)',
          width: '100%',
        }}
      >
        <ActionIcon
          variant="outline"
          color={colorScheme === 'dark' ? 'yellow' : 'blue'}
          onClick={() => toggleColorScheme()}
          title="Toggle color scheme"
          size="lg"
        >
          {colorScheme === 'dark' ? <IconSun size={20} /> : <IconMoon size={20} />}
        </ActionIcon>
      </Group>

      {/* Animated title */}
      <h1
        style={{
          fontSize: '4rem',
          fontWeight: 700,
          background: `linear-gradient(90deg, ${crumblePrimary[4]}, ${crumblePrimary[5]}, ${crumblePrimary[6]})`,
          backgroundSize: '200% auto',
          color: 'transparent',
          backgroundClip: 'text',
          WebkitBackgroundClip: 'text',
          animation: 'shine 3s linear infinite',
          marginBottom: '2rem',
        }}
      >
        Crumblesworth
      </h1>

      <Text size="lg" mb="xl">
        Welcome to the ultimate bakery management app — recipes, inventory, and COGs made easy.
      </Text>

      {/* Cookie component above feature cards */}
      <Cookie />

      {/* Feature cards */}
      <div
        style={{
          display: 'flex',
          flexWrap: 'wrap',
          gap: '2rem',
          justifyContent: 'center',
          marginTop: '2rem',
        }}
      >
        {features.map((feature, index) => (
          <motion.div
            key={feature}
            initial="offscreen"
            whileInView="onscreen"
            viewport={{ once: true, amount: 0.8 }}
            variants={cardVariants}
            style={{
              width: 180,
              height: 120,
              display: 'flex',
              justifyContent: 'center',
              alignItems: 'center',
              borderRadius: 16,
              background: crumblePrimary[index % crumblePrimary.length],
              color: '#2c1f12',
              fontWeight: 700,
              fontSize: '1.2rem',
              boxShadow: '0 4px 12px rgba(0,0,0,0.1)',
            }}
          >
            {feature}
          </motion.div>
        ))}
      </div>

      {/* Shine animation */}
      <style>
        {`
          @keyframes shine {
            0% { background-position: 0% 50%; }
            100% { background-position: 200% 50%; }
          }
        `}
      </style>
    </Container>
  );
}