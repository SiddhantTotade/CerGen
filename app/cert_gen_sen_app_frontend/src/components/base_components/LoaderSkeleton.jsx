import * as React from 'react';
import Skeleton from '@mui/material/Skeleton';

export default function LoaderSkeleton(props) {

    const padding = props.barPadding
    const width = props.barWidth

    return (
        <Skeleton animation="wave" sx={{ padding: padding, width: width }} />
    );
}