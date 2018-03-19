export default {
  TOSAST_STATE(state, opt) {
    let msg = {...opt}
    state.toastText = msg.text
    state.toastTime = msg.time || 1000
  }
}
