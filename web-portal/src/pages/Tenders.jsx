import React from 'react';
import { Typography, Card, CardContent, Button, Grid } from '@mui/material';

const tenders = [
  { id: 1, title: 'Road Tender', deadline: '2025-01-01', pdf: 'http://example.com/tender1.pdf' },
];

export default function Tenders() {
  return (
    <div>
      <Typography variant="h5" gutterBottom>Latest Tenders</Typography>
      <Grid container spacing={2}>
        {tenders.map(tender => (
          <Grid item xs={12} md={6} key={tender.id}>
            <Card>
              <CardContent>
                <Typography variant="h6">{tender.title}</Typography>
                <Typography>Deadline: {tender.deadline}</Typography>
                <Button
                  variant="outlined"
                  color="secondary"
                  href={`https://wa.me/254700000000?text=I%20want%20to%20bid%20on%20${encodeURIComponent(tender.title)}`}
                  target="_blank"
                  sx={{ mt: 1 }}
                >
                  Bid via WhatsApp
                </Button>
                <Button
                  variant="text"
                  href={tender.pdf}
                  target="_blank"
                  sx={{ ml: 2 }}
                >
                  View PDF
                </Button>
              </CardContent>
            </Card>
          </Grid>
        ))}
      </Grid>
    </div>
  );
} 