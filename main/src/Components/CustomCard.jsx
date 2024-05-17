import React from 'react'
import IconButton from '@mui/material/IconButton';
import ArrowForwardIcon from '@mui/icons-material/ArrowForward';
import { Button } from '@mui/material';
const CustomCard = ({icon,title="Data Center",content="",content1="",border=true,swap=false,link=""}) => {
  return (
    <div className={'d-flex flex-column justify-content-center align-items-start p-4 pb-0 Card-show '+ (border==false?"no-border" : "")} >
                <div className='mb-4 d-flex justify-content-start align-items-start h-25'>
                {icon}

                </div>
                <div className='d-flex flex-column justify-content-center align-items-start h-75'>
                    {swap==true?(<>
                        <span className='content' style={{color:"var(--main)"}}>
                      {content}

                  </span>
                    <span className='bold-content-big'>
                  {title}
              </span>
              <span className='content' style={{fontSize:"12px"}}>
                      {content1}

                  </span>
              
                  </>):(<>
                  <span className='bold-content-big'>
                      {title}
                  </span>
                  <span className='content' style={{color:"var(--main)"}}>
                          {content}

                      </span></>)}
                      <Button variant='outlined' className='intro-button mt-3' href={link}>Read More</Button>
                {/* <IconButton>
                    <ArrowForwardIcon style={{color:"var(--wt)",fontSize:"50px"}} ></ArrowForwardIcon>
                </IconButton> */}
                </div>
            </div>
  )
}

export default CustomCard