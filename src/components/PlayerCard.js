import React, { useState } from "react";
// import cardBackground from "./images/background-card.jpg";

const PlayerCard = () => {
    const [playerName, setPlayerName] = useState('Mike')
    const [backgroundImg, setBackgroundImg] = useState('')
    const [flagImage, setFlagImage] = useState('')
    const [playerImage, setPlayerImage] = useState('')
    // console.log(cardBackground)
    // let image = 'https://cdn.discordapp.com/attachments/693920868220403742/1064964877787086979/background-card.jpg'
    return(
        <>
        <div>
            <div style={{width: "350px", height: "500px",
             borderColor: "white", backgroundImage: `url("https://via.placeholder.com/500")` }}>
            "HI"
            </div>
        </div>
        </>
    )
}

export default PlayerCard;