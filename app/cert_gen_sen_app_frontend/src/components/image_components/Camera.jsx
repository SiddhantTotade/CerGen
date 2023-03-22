import React from 'react'
import Webcam from 'react-webcam'

const videoConstraints = {
    width: 1280,
    height: 720,
    facingMode: "environment"
};

export const Camera = () => {
    const webCamRef = React.useRef(null)
    const [imgSrc, setImgSrc] = React.useState(null)
    const capture = React.useCallback(
        () => {
            const imageSrc = webCamRef.current.getScreenshot({ width: 1920, height: 1080 });
            setImgSrc(imageSrc)
        },
        [webCamRef, setImgSrc]
    );

    return (
        <Webcam
            audio={false}
            height={720}
            ref={webCamRef}
            screenshotFormat="image/jpeg"
            width={1280}
            videoConstraints={videoConstraints}
        />
    )
}
