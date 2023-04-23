import React, { useState } from 'react'
import '../../album.css'
import CloseIcon from '@mui/icons-material/Close';
import { getToken } from '../../services/LocalStorageService';
import { useGetAlbumImagesQuery } from '../../services/participantsImagesAPI';
import LoaderSkeleton from '../base_components/LoaderSkeleton';

export const Album = (props) => {

    const { access_token } = getToken()

    const { data = [], isLoading } = useGetAlbumImagesQuery({ access_token: access_token, event_slug: props.event_slug })

    const [model, setModel] = useState(false)

    const [tempImg, setTempImg] = useState("")

    const getImg = (imgSrc) => {
        setTempImg(imgSrc)
        setModel(true)
    }

    return (
        <>
            {
                data !== "Failed to get images" ?
                    <div>
                        {
                            isLoading ? <LoaderSkeleton barWidth="20%" barPadding="10%" /> :
                                <div className={model ? 'model open' : 'model'}>
                                    <img src={'http://127.0.0.1:8000' + tempImg} alt="" />
                                    <CloseIcon onClick={() => setModel(false)} />
                                </div>
                        }
                        <div className='gallery'>
                            {data.map((item, index) => {
                                return <div className='pics' key={index} onClick={() => getImg(item.image_album)}>
                                    <img src={'http://127.0.0.1:8000' + item.image_album} alt="" style={{ width: "100%", borderRadius: '5px', border: '2px solid gray' }} />
                                </div>
                            })}
                        </div>
                    </div> : "No images found"
            }
        </>
    )
}
