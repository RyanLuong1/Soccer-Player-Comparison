import React, { useState } from "react";
import cardBackground from "../images/background-card.jpg";

const PlayerCard = () => {
    const [playerName, setPlayerName] = useState('Mike')
    const [backgroundImg, setBackgroundImg] = useState('')
    const [flagImage, setFlagImage] = useState('')
    const [playerImage, setPlayerImage] = useState('')
    // console.log(cardBackground)

    return(
        <>
        <div>
            <div style={{width: "350px", height: "500px",
             borderColor: "white", borderRadius: "3px", borderStyle: "solid",
             backgroundImage: "url("+{cardBackground}+")",
             backgroundSize: 'cover' }}>
            {/* <img src={{cardBackground}}/> */}

            </div>
        </div>
        </>
    )
}

export default PlayerCard;