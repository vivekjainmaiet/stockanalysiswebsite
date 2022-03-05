import React from "react";
import { LineChart, Line, CartesianGrid, XAxis, YAxis, Tooltip } from 'recharts';

const data = [{name: '400', uv: 400}, {name: '600', uv: 600},{name: '800', uv: 800},];

export default function Graph() {

  return (

<div className = 'lstm_model' >

<h1>Our Prediction for Today is ###:</h1>

<LineChart width={750} height={400} data={data} margin={{ top: 30, right: 20, bottom: 10, left: 0 }}>
    <Line type="monotone" dataKey="uv" stroke="#8884d8" />
    <CartesianGrid stroke="#ccc" strokeDasharray="5 5" />
    <XAxis dataKey="name" />
    <YAxis />
    <Tooltip />
  </LineChart>

  </div>
);
  }
