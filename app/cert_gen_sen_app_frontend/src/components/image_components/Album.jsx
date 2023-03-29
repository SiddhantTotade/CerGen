import React, { useState } from 'react'
import { useEffect } from 'react';
import axios from 'axios';
import '../../index.scss'
import PhotoAlbum from 'react-photo-album'

export const Album = (props) => {

    const [albumImages, setAlbumImages] = useState([])

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
        <div>
            {
                albumImages.map((img, id) => {
                    return <PhotoAlbum layout='rows' key={id} photos={[{ href: 'http://127.0.0.1:8000' + img.image_album }]} />
                })
            }
        </div>
    )
}
