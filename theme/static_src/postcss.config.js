module.exports = {
  plugins: {
    "postcss-import": {},
    "postcss-simple-vars": {},
    "postcss-nested": {}
  },
  theme: {
    extend: {
        'dark-main': '#18191A',
        'dark-second': '#242526',
        'dark-third': '#3A3B3C',
        'dark-txt': '#B8BBBF',
        sky: colors.sky,
        teal: colors.teal,
        rose: colors.rose,
    },
  },
  variants: {
    extend: {
        display: ['group-hover'],
        transform: ['group-hover'],
        scale: ['group-hover'],
        textOpacity: ['dark'],
    },
  },
}
