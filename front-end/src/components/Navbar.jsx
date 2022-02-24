import React from 'react';
import {BiSearchAlt} from 'react-icons/bi';
import {FiBell} from 'react-icons/fi';
import {BsFillCaretDownFill} from 'react-icons/bs';
import avatar from '../assets/avatarImage.jpeg';

export default function Navbar() {
  return (
    <div className='navbar'>

        <div className= 'title'>
            <h2>DASHBOARD</h2>
            <span>Stocks Predictions Everyday</span>
        </div>



        <div className= 'container'>

                <div className='search'>
                     <BiSearchAlt/>
                     <input type='text' placeholder='Search ...'/>
                </div>

                <button>PREDICT</button>

                <div className= 'profile'>

                      <FiBell className='bell'/>

                      <div className='image'>
                      <img src={avatar} alt='' />
                      </div>

                      <div className='profile__name'>
                      <h4>Loris Liusso</h4>
                      <h6>Admin</h6>
                      </div>

                      <BsFillCaretDownFill/>


                </div>


      </div>



  </div>
  );
}
