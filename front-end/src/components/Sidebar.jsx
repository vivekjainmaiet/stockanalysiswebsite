import React from 'react'
import Links from './Links'
import {FiShoppingBag, FiSettings} from "react-icons/fi";
import { HiOutlineShoppingCart } from "react-icons/hi";
import { GiSchoolBag } from "react-icons/gi";
import {IoWalletOutline } from "react-icons/io5";
import { RiTruckLine } from "react-icons/ri";
import { BiHelpCircle } from "react-icons/bi";
import { MdLogout } from "react-icons/md";
import rocket from "../assets/rocket.png";


export default function Sidebar() {
  const links1= [
    {
      text:'Home',
      icon: FiShoppingBag,
      active:true,
    },

    {
      text: '########',
      icon: HiOutlineShoppingCart,
    },

    {
      text: '#########',
      icon: GiSchoolBag,
    },

    {
      text: '########',
      icon: IoWalletOutline,
    },

    {
      text: '#########',
      icon: RiTruckLine,
    },

  ];

const links2= [

  {
    text: 'Help Center',
    icon: BiHelpCircle,
  },

  {
    text: 'Settings',
    icon: FiSettings,
  },

  {
    text: 'Logout',
    icon: MdLogout,
  },

];


  return (
    <div className= 'sidebar'>
<div className='brand'>StockAnalysis</div>
  <div className='links'>
  <Links links={links1} />
   <Links links={links2} />
      </div>



<div className='pro'>
      <div className='image'>

        <img src={rocket} alt='rocket' />
        </div>

      <h3> DASHBOARD PRO</h3>

      <h4>Get access to all features:</h4>

      <button className='button'>Get Pro!</button>

      </div>

    </div>
  );
}
