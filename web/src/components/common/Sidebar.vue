<template>
  <div class="sidebar">
    <el-menu
      class="el-menu-vertical-demo"
      :default-active="onRoutes"
      unique-opened
      router
      background-color="#2E363F"
      text-color="#fff"
      active-text-color="#ffd04b">
      <template v-for="item in items">
        <template v-if="item.subs">
          <el-submenu :index="item.index">
            <template slot="title"><i :class="item.icon"></i>{{ item.title }}</template>
            <el-menu-item v-for="(subItem,i) in item.subs" :key="i" :index="subItem.index">
              <i :class="subItem.icon"></i>
              {{ subItem.title }}
            </el-menu-item>
          </el-submenu>
        </template>
        <template v-else>
          <el-menu-item :index="item.index">
            <i :class="item.icon"></i>{{ item.title }}
          </el-menu-item>
        </template>
      </template>
    </el-menu>
  </div>
</template>

<script>
  export default {
    data() {
      return {
        items: [
          {
            icon: 'el-icon-menu',
            index: '1',
            title: '库存',
            subs: [
              {
                index: 'stock_new',
                title: '新建库存',
                icon: 'el-icon-edit-outline',
              },
              {
                index: 'stock_list',
                title: '库存列表',
                icon: 'el-icon-tickets',
              },
            ]
          },
          {
            icon: 'el-icon-menu',
            index: '2',
            title: '模板',
            subs: [
              {
                index: 'template_new',
                title: '新建模板',
                icon: 'el-icon-edit-outline',
              },
              {
                index: 'template_list',
                title: '模板列表',
                icon: 'el-icon-tickets',
              }
            ]
          },
          {
            icon: 'el-icon-menu',
            index: '3',
            title: '客户',
            subs: [
              {
                index: 'customer_new',
                title: '添加客户',
                icon: 'el-icon-edit-outline',
              },
              {
                index: 'customer_list',
                title: '客户列表',
                icon: 'el-icon-tickets',
              }
            ]
          },
          {
            icon: 'el-icon-menu',
            index: '4',
            title: '管理员',
            subs: [
              {
                index: 'admin_list',
                title: '管理员列表',
                icon: 'el-icon-tickets',
              },
              {
                index: 'admin_new',
                title: '新建管理员',
                icon: 'el-icon-edit-outline',
              },
            ]
          },
        ]
      }
    },
    computed: {
      onRoutes() {
        return this.$route.path.replace('/', '');
      }
    }
  }
</script>

<style scoped>
  .sidebar {
    display: block;
    position: absolute;
    width: 250px;
    left: 0;
    top: 70px;
    bottom: 0;
  }

  .sidebar > ul {
    height: 100%;
  }
</style>
