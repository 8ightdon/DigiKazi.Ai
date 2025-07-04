import React from 'react';
import { Typography, Card, CardContent, Grid } from '@mui/material';

const metrics = [
  { label: 'Gigs Matched', value: 120 },
  { label: 'Tenders Alerted', value: 45 },
  { label: 'Emergencies Handled', value: 10 },
];

const testimonials = [
  { name: 'Ali', text: 'Nimepata kazi haraka sana, asante DigiKazi!' },
  { name: 'Jane', text: 'Tender alerts zimenisaidia sana kupata deals.' },
];

export default function Impact() {
  return (
    <div>
      <Typography variant="h5" gutterBottom>Impact Metrics</Typography>
      <Grid container spacing={2}>
        {metrics.map((m, i) => (
          <Grid item xs={12} md={4} key={i}>
            <Card>
              <CardContent>
                <Typography variant="h6">{m.value}</Typography>
                <Typography>{m.label}</Typography>
              </CardContent>
            </Card>
          </Grid>
        ))}
      </Grid>
      <Typography variant="h6" sx={{ mt: 4 }}>Testimonials</Typography>
      {testimonials.map((t, i) => (
        <Card key={i} sx={{ my: 2 }}>
          <CardContent>
            <Typography>"{t.text}"</Typography>
            <Typography variant="caption">- {t.name}</Typography>
          </CardContent>
        </Card>
      ))}
    </div>
  );
} 