import {setStore,removeStore,getStore} from "../utils/storage";

export default {
  TOSAST_STATE(state, opt) {
    let msg = {...opt}
    state.toastText = msg.text
    state.toastTime = msg.time || 1000
  },
  GET_USERINFO(state){
    if (!state.userInfo && getStore('userInfo')) {
      state.userInfo = JSON.parse(getStore('userInfo'))
    }
  },
  REWRITE_USERINFO(state,info){
    state.userInfo = info
    setStore('userInfo', info)
  },
  REMOVE_USERINFO(state) {
    state.userInfo = null
    removeStore('userInfo')
  }

}
