import { Routes, Route } from 'react-router-dom';
import HomePage from './pages/Home';
import { NavbarNested } from './pages/NavBarNested';

export default function App() {
  return (
<div className="crumbleBackground" style={{ display: 'flex', minHeight: '100vh' }}>
  <NavbarNested /> {/* fixed width sidebar */}
  <div style={{ flex: 1, padding: '2rem' }}>
    <Routes>
      <Route path="/" element={<HomePage />} />
      {/* other routes */}
    </Routes>
  </div>
</div>
  );
}