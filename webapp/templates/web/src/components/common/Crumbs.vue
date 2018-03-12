<template>
    <div class="crumbs">
      <el-breadcrumb separator="/">
        <el-breadcrumb-item><i class="el-icon-menu"></i> {{crumbs1}}</el-breadcrumb-item>
        <el-breadcrumb-item>{{crumbs2}}</el-breadcrumb-item>
      </el-breadcrumb>
    </div>
</template>

<script>
export default {
  props: {
    crumbs1: {
      type: String,
      default: ""
    },
    crumbs2: {
      type: String,
      default: ""
    }
  }
}
</script>
