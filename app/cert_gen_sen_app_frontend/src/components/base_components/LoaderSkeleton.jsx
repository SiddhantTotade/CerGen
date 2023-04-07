import * as React from 'react';
import Box from '@mui/material/Box';
import Skeleton from '@mui/material/Skeleton';

export default function LoaderSkeleton(props) {

    const width = props.barWidth

    return (
        <Box sx={{ width: 300 }}>
            <Skeleton animation="wave" sx={{ padding: width }} />
        </Box>
    );
}