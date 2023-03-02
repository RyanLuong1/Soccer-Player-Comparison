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
                <div style={{flex: 3.5, backgroundImage: "url(https://media.discordapp.net/attachments/693920868220403742/1080218735417229483/player-card-top-05.jpg?width=907&height=515)",
                backgroundSize: "cover"}}>
                    <img style={{width: "200px", height: "200px"}} src="https://media.discordapp.net/attachments/693920868220403742/1080205853686251631/image.png">
                    </img>
                </div>

                <div style={{flex: 1, textAlign: "center", backgroundImage: "url(https://media.discordapp.net/attachments/693920868220403742/1080219324083609610/player-card-mid-06.jpg?width=949&height=117)"}}>
                Cristano Ronaldo
                </div>

                <div className="stats" style={{flex: 5.5, backgroundColor: "blue", backgroundImage: "url(https://media.discordapp.net/attachments/693920868220403742/1080925124812886157/player-card-bottom-07.jpg?width=636&height=467)",
            backgroundSize: "cover"}}>
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