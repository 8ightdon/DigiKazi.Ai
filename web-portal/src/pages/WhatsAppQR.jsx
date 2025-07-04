import React from 'react';
import { Typography, Box } from '@mui/material';

export default function WhatsAppQR() {
  return (
    <Box textAlign="center">
      <Typography variant="h5" gutterBottom>Join DigiKazi on WhatsApp</Typography>
      <img
        src="https://api.qrserver.com/v1/create-qr-code/?size=200x200&data=https://wa.me/254700000000?text=Hi%20DigiKazi!"
        alt="WhatsApp QR"
        style={{ margin: '20px 0' }}
      />
      <Typography>Scan to chat with DigiKazi AI-Bot on WhatsApp!</Typography>
    </Box>
  );
} 