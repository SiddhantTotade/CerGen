import * as React from 'react';
import Skeleton from '@mui/material/Skeleton';

export default function LoaderSkeleton(props) {

    const padding = props.barPadding

    return (
        <Skeleton animation="wave" sx={{ padding: padding }} />
    );
}