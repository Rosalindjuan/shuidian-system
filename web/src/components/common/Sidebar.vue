<template>
    <div class="sidebar">
        <el-menu :default-active="onRoutes" class="el-menu-vertical-demo" theme="dark" unique-opened router>
            <template v-for="item in items">
                <template v-if="item.subs">
                    <el-submenu :index="item.index">
                        <template slot="title"><i :class="item.icon"></i>{{ item.title }}</template>
                        <el-menu-item v-for="(subItem,i) in item.subs" :key="i" :index="subItem.index">{{ subItem.title }}
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
//                    {
//                        icon: 'el-icon-setting',
//                        index: 'readme',
//                        title: '自述'
//                    },
                    {
                        icon: 'el-icon-menu',
                        index: '2',
                        title: '库存管理',
                        subs: [
                            {
                                index: 'readme',
                                title: '库存列表'
                            },
                            {
                                index: 'vuetable',
                                title: '新建库存'
                            }
                        ]
                    },
                    {
                        icon: 'el-icon-menu',
                        index: '3',
                        title: '模板',
                        subs: [
                            {
                                index: 'baseform',
                                title: '模板列表'
                            },
                            {
                                index: 'vueeditor',
                                title: '新建模板'
                            },
                        ]
                    },
                  {
                    icon: 'el-icon-date',
                    index: '4',
                    title: '客户管理',
                    subs: [
                      {
                        index: 'baseform',
                        title: '客户列表'
                      },
                      {
                        index: 'vueeditor',
                        title: '新建客户'
                      },
                    ]
                  },
                  {
                    icon: 'el-icon-date',
                    index: '5',
                    title: '管理员',
                    subs: [
                      {
                        index: 'baseform',
                        title: '管理员列表'
                      },
                      {
                        index: 'vueeditor',
                        title: '新建管理员'
                      },
                    ]
                  },
                ]
            }
        },
        computed:{
            onRoutes(){
                return this.$route.path.replace('/','');
            }
        }
    }
</script>

<style scoped>
    .sidebar{
        display: block;
        position: absolute;
        width: 250px;
        left: 0;
        top: 70px;
        bottom:0;
        background: #2E363F;
    }
    .sidebar > ul {
        height:100%;
    }
</style>
