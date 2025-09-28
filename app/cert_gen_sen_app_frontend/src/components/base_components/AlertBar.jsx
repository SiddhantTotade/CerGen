import React from 'react'
import { Alert, Stack } from '@mui/material'

const AlertBar = (props) => {

    const width = props.barWidth

    return (
        <Stack sx={{ width: width, display: 'flex', justifyContent: 'flex-start' }} spacing={10}>
            <Alert severity={props.severity}>{props.message}</Alert>
        </Stack>
    )
}

export default AlertBar