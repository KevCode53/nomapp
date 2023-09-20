import './sidebar.css'
import {useAuth} from '../../hooks/useAuth'
import {RiBuilding2Fill, RiUser2Fill, RiLogoutCircleFill, RiCloseCircleLine} from "react-icons/ri";
import {menuSubject} from '../../services/show-menu-subject.service'
import { useEffect, useState } from 'react';

export const Sidebar = () => {

  const [showMenu, setShowMenu] = useState(false)

  const {user, handleLogout} = useAuth()

  const handleCloseMenu = () => {
    menuSubject.setSubject(false)
  }

  useEffect(() => {
    menuSubject.getSubject().subscribe((value) => {
      setShowMenu(value)
    })
  },[])

  return (
    <aside className={`${showMenu && 'show'} sidebar_wrapper`}>
      <div className="sidebar__content bg-gradient-to-b from-indigo-800 via-purple-700 to-pink-900  h-full">
        <button onClick={handleCloseMenu} className="sidebar__btn_close text-5xl text-gray-50">
          <RiCloseCircleLine/>
        </button>
        <div className="sidebar__user_info">
          <picture>
            {user?.image
              ? (<img className='bg-gray-100 rounded-full' src={`http://127.0.0.1:8000${user?.image}`} alt="" />) 
              : (<img src={user?.url_img} alt="" />)
            }
          </picture>
          <h3 className=' text-xl text-gray-50 font-bold' >{`${user?.name} ${user?.last_name}`}</h3>
          <span className='text-gray-400'>{user?.email}</span>
        </div>
        <div className="sidebar__menu">
          <ul className="menu_list">
            <li className="menu_item">
              <a href="" className="menu_link text-2xl font-bold text-gray-300">
                <RiBuilding2Fill/>
                <span>
                  Empresas
                </span>
              </a>
            </li>
            <li className="menu_item">
              <a href="" className="menu_link text-2xl font-bold text-gray-300">
                <RiUser2Fill/>
                <span>
                  Empleados
                </span>
              </a>
            </li>
            <li className="menu_item">
              <button onClick={handleLogout} className="menu_link text-2xl font-bold text-gray-300">
                <RiLogoutCircleFill />
                <span>
                  Salir
                </span>
              </button>
            </li>
          </ul>
        </div>
      </div>
    </aside>
  )
}
