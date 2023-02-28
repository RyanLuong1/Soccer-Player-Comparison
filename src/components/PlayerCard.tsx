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
            <div style={{ width: "350px", height: "500px", flexDirection: "column", display: "flex",
             borderColor: "white", backgroundImage: `url("https://via.placeholder.com/500")` }}>
                <div style={{flex: 3.5, backgroundColor: "red", backgroundImage: "url(https://media.discordapp.net/attachments/693920868220403742/1080207383088877668/player-card-top-05.jpg?width=824&height=468)",
                backgroundSize: "cover"}}>
                    <img style={{width: "200px", height: "200px"}} src="https://media.discordapp.net/attachments/693920868220403742/1080205853686251631/image.png">
                    </img>
                </div>

                <div style={{flex: 1, backgroundColor: "gray", textAlign: "center"}}>
                Player Name
                </div>

                <div className="stats" style={{flex: 5.5, backgroundColor: "blue"}}>
                    <div className="grid grid-cols-2 gap-3">
                        <div>01</div>
                        <div>02</div>
                        <div>03</div>
                        <div>04</div>
                        <div>05</div>
                        <div>06</div>
                    </div>
                </div>
            </div>
        </div>
        </>
    )
}

export default PlayerCard;