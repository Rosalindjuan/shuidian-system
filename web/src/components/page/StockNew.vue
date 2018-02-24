<template>
  <div>
    <Crumbs crumbs1="库存" crumbs2="新建库存"></Crumbs>
    <div class="form-box">
      <el-form ref="form" :model="form" label-width="80px">
        <el-form-item label="名称">
          <el-input v-model="form.name"></el-input>
        </el-form-item>
        <el-form-item label="数量">
          <el-input v-model="form.num"></el-input>
        </el-form-item>
        <el-form-item label="添加数量">
          <el-input v-model="form.addNum"></el-input>
        </el-form-item>
        <el-form-item label="单位">
          <el-input v-model="form.unit"></el-input>
        </el-form-item>
        <el-form-item label="进价">
          <el-input v-model="form.opening_price"></el-input>
        </el-form-item>
        <el-form-item label="单价">
          <el-input v-model="form.price"></el-input>
        </el-form-item>
        <el-form-item label="备注">
          <el-input type="textarea" v-model="form.remarks"></el-input>
        </el-form-item>
        <el-form-item>
          <el-button type="primary" @click="onSubmit">提交</el-button>
          <!--<el-button>取消</el-button>-->
        </el-form-item>
      </el-form>
    </div>
  </div>
</template>

<script>
  import Crumbs from "../common/Crumbs.vue"
  export default {
    components: {
      Crumbs
    },
    data() {
      return {
        form: {
          name: '',
          num: 0,
          addNum: 0,
          unit: '',
          opening_price: '',
          price: '',
          remarks: '',
        }
      }
    },
    methods: {
      onSubmit() {
        console.log("submit")
      }
    }
  }
</script>

<style scoped>
  .form-box {
    padding-top: 20px;
  }
</style>
