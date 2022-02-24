import React from 'react';
import Navbar from './Navbar';
import Milestones from './Milestones';
import Lstm from './Lstm';
import Twitter from './Twitter';
import Indicators from './Indicators';
import News from './News';
import Graph from './Graph';



export default function Dashboard() {
  return (
    <div className='dashboard'>

          <Navbar />

          <div className='grid'>

              <div className='one'>
              <Milestones/>
              </div>

               <div className='two'>
               <Twitter />
               <Graph />
               </div>


               <div className = 'three'>
                 <News />
                 <Indicators />
                 </div>

                <div className='copyright'>
                   <p > COPYRIGHT © STOCKANALYSIS - LE WAGON PROJECT 2022 </p>

                </div>




          </div>



    </div>
  );
}
