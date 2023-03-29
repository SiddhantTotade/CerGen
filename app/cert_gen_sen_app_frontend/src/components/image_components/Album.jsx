import React, { useState } from 'react'
import { useEffect } from 'react';
import axios from 'axios';
import '../../album.css'
import CloseIcon from '@mui/icons-material/Close';

export const Album = (props) => {

    const [albumImages, setAlbumImages] = useState([])

    const [model, setModel] = useState(false)
    const [tempImg, setTempImg] = useState("")
    const getImg = (imgSrc) => {
        setTempImg(imgSrc)
        setModel(true)
    }

    useEffect(() => {

        const url = 'http://127.0.0.1:8000/api/upload-event-album/' + props.event_slug

        axios
            .get(url, {
                headers: { Authorization: "Token " + localStorage.getItem("token") },
            }).then(res => setAlbumImages(res.data)).catch(err => console.log(err))
    }, [props.event_slug]);

    return (
        // <div className='gallery'>
        //     <div className='gallery__column'>
        //         <figure className='gallery__thumb flex gap-4'>
        //             {albumImages.map((img, id) => {
        //                 return <img key={id} src={'http://127.0.0.1:8000' + img.image_album} alt="" className='gallery__image h-full object-contain' />
        //             })}
        //         </figure>
        //     </div>
        // </div>
        <>
            <div className={model ? 'model open' : 'model'}>
                <img src={'http://127.0.0.1:8000' + tempImg} alt="" />
                <CloseIcon onClick={() => setModel(false)} />
            </div>
            <div className='gallery'>
                {albumImages.map((item, index) => {
                    return <div className='pics' key={index} onClick={() => getImg(item.image_album)}>
                        <img src={'http://127.0.0.1:8000' + item.image_album} alt="" style={{ width: "100%", borderRadius: '5px', border: '2px solid gray' }} />
                    </div>
                })}
            </div>
        </>
    )
}
