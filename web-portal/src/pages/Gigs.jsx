import React from 'react';
import { Typography, Card, CardContent, Button, Grid } from '@mui/material';

const gigs = [
  { id: 1, title: 'Plumber Job', location: 'Nairobi', pay: 1000 },
  { id: 2, title: 'Electrician Needed', location: 'Mombasa', pay: 1500 },
];

export default function Gigs() {
  return (
    <div>
      <Typography variant="h5" gutterBottom>Available Gigs</Typography>
      <Grid container spacing={2}>
        {gigs.map(gig => (
          <Grid item xs={12} md={6} key={gig.id}>
            <Card>
              <CardContent>
                <Typography variant="h6">{gig.title}</Typography>
                <Typography>Location: {gig.location}</Typography>
                <Typography>Pay: KES {gig.pay}</Typography>
                <Button
                  variant="outlined"
                  color="primary"
                  href={`https://wa.me/254700000000?text=I%20want%20to%20apply%20for%20${encodeURIComponent(gig.title)}`}
                  target="_blank"
                  sx={{ mt: 1 }}
                >
                  Apply via WhatsApp
                </Button>
              </CardContent>
            </Card>
          </Grid>
        ))}
      </Grid>
    </div>
  );
} 