import { Routes, Route } from 'react-router-dom';
import HomePage from './pages/Home';

export default function App() {
  return (
    <Routes>
      <Route path="/" element={<HomePage />} />
      {/* Add more routes here if needed */}
    </Routes>
  );
}