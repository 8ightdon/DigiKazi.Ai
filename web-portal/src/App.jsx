import React, { useState } from 'react';
import { AppBar, Toolbar, Typography, Tabs, Tab, Box, Container, Button } from '@mui/material';
import Onboarding from './pages/Onboarding';
import Gigs from './pages/Gigs';
import Tenders from './pages/Tenders';
import Impact from './pages/Impact';
import WhatsAppQR from './pages/WhatsAppQR';

const pages = [
  { label: 'Onboarding', component: <Onboarding /> },
  { label: 'Gigs', component: <Gigs /> },
  { label: 'Tenders', component: <Tenders /> },
  { label: 'Impact', component: <Impact /> },
  { label: 'WhatsApp QR', component: <WhatsAppQR /> },
];

export default function App() {
  const [tab, setTab] = useState(0);

  return (
    <Box sx={{ flexGrow: 1 }}>
      <AppBar position="static">
        <Toolbar>
          <Typography variant="h6" sx={{ flexGrow: 1 }}>
            DigiKazi Web Portal
          </Typography>
        </Toolbar>
        <Tabs value={tab} onChange={(_, v) => setTab(v)} centered>
          {pages.map((p, i) => (
            <Tab label={p.label} key={p.label} />
          ))}
        </Tabs>
      </AppBar>
      <Container sx={{ mt: 4 }}>
        {pages[tab].component}
      </Container>
    </Box>
  );
} 