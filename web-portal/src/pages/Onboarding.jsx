import React from 'react';
import { Typography, Button, Box } from '@mui/material';

export default function Onboarding() {
  return (
    <Box>
      <Typography variant="h5" gutterBottom>
        Welcome to DigiKazi!
      </Typography>
      <Typography gutterBottom>
        Join our WhatsApp bot to start finding gigs, tenders, and more. No app install needed!
      </Typography>
      <Button
        variant="contained"
        color="success"
        href="https://wa.me/254700000000?text=Hi%20DigiKazi!"
        target="_blank"
      >
        Join WhatsApp Bot
      </Button>
    </Box>
  );
} 