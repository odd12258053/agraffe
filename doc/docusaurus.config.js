module.exports = {
  title: 'Agraffe',
  tagline: 'build API with ASGI in Serverless services',
  url: 'https://agraffe.info',
  baseUrl: '/',
  onBrokenLinks: 'throw',
  onBrokenMarkdownLinks: 'warn',
  favicon: 'img/icon.png',
  organizationName: 'odd12258053',
  projectName: 'agraffe',
  customFields: {
    sourceUrl: 'https://github.com/odd12258053/agraffe',
    description:
      'Agraffe, build API with ASGI in Serverless services (e.g AWS lambda, Google Cloud Functions and Azure Functions).',
  },
  themeConfig: {
    navbar: {
      title: 'Agraffe',
      logo: {
        alt: 'Logo',
        src: 'img/icon.png',
      },
      items: [
        {
          to: 'docs/',
          activeBasePath: 'docs',
          label: 'Docs',
          position: 'left',
        },
        {
          href: 'https://github.com/odd12258053/agraffe',
          label: 'GitHub',
          position: 'right',
        },
      ],
    },
    footer: {
      style: 'dark',
      links: [],
      copyright: `Copyright © ${new Date().getFullYear()} odd12258053. Built with Docusaurus.`,
    },
    colorMode: {
      disableSwitch: true,
    },
    sidebarCollapsible: false,
    image: 'img/icon.png',
    // metadatas: [
    //   {name: 'description', content: },
    //   {name: 'og:description', content: 'Agraffe, build API with ASGI in Serverless services (e.g AWS lambda, Google Cloud Functions and Azure Functions).'},
    // ]
  },
  presets: [
    [
      '@docusaurus/preset-classic',
      {
        docs: {
          sidebarPath: require.resolve('./sidebars.js'),
          editUrl: 'https://github.com/odd12258053/agraffe/edit/master/doc/',
        },
        theme: {
          customCss: require.resolve('./src/css/custom.css'),
        },
      },
    ],
  ],
}
