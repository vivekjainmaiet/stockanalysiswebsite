import React from 'react';
import {AiOutlineStock} from 'react-icons/ai';



export default function Milestones() {

  const data= [

{

icon: AiOutlineStock,
title: 'Today Price STOCK ',
value: '###',
},

    {

      icon: AiOutlineStock,
      title: 'Yesterday Price STOCK ',
      value: '###',
    },


    {

      icon: AiOutlineStock,
      title: 'Last Week Price STOCK',
      value: '###',
    },


    {

      icon: AiOutlineStock,
      title: 'Last Month Price STOCK',
      value: '###',
    },


  ];


  return (

  <div className='milestones'>

    {
      data.map((milestone)=> {

      return (

        <div className='milestone'>
        <div className='icon'>
        <milestone.icon/>

        </div>

        <div className='details'>
        <h4>{milestone.title}</h4>
          <h2>{milestone.value}</h2>

        </div>

        </div>
      );

    })
    }
      </div>
  );
}
