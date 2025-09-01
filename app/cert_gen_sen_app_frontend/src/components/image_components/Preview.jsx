import React from 'react'

export const Preview = (props) => {
    console.log(props.imgSrc);
    return (
        <div>
            <img src={props.imgSrc} alt="" />
        </div>
    )
}
