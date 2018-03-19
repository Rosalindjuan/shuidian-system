<template>
  <!--吐司组件-->
  <span>
    <transition name="fade">
      <span class="pop-msg" v-if="popMsg">{{toastText}}</span>
    </transition>
  </span>
</template>
<script>
  import {mapState, mapMutations} from 'vuex'
  export default {
    props: {},
    data () {
      return {
        timer: null
      }
    },
    computed: {
      ...mapState(['toastText', 'toastTime']),
      // 是否显示弹窗`
      popMsg () {
        if (this.toastText) {
          this.timer = setTimeout(() => {
            clearTimeout(this.timer)
            this.TOSAST_STATE({text: ''})
          }, this.toastTime)
        }
        return this.toastText ? 1 : 0
      }
    },
    methods: {
      ...mapMutations(['TOSAST_STATE'])
    },
    created () {
    }
  }
</script>
<style scoped>
  @import '../../../static/css/animation.scss';
  span.pop-msg {
    text-align: center;
    z-index: 99999999;
    position: fixed;
    top: 40%;
    left: 50%;
    transform: translateX(-50%);
    display: flex;
    padding: .4rem .4rem;
    color: #fff;
    background: rgba(0, 0, 0, .6);
  }
</style>


